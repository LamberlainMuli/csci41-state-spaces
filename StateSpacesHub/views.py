from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Building, Venue, Amenity, Agent, TeamMember, Customer, Reservation, Renovation
from .forms import BuildingForm, VenueForm, AmenityForm, VenueFormSet,VenueFormHelper, AmenityFormSet, AmenityFormHelper
from django.http import HttpResponseRedirect


class HomePage(ListView):
    model = Building
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['buildings'] = Building.objects.all()
        context['total_buildings'] = Building.objects.count()
        context['recent_buildings'] = Building.objects.order_by('-id')[:5]  
        context['agents'] = Agent.objects.all()[:3]
        context['description'] = ['Ensuring state-of-the-art facilities and maintaining customer satisfaction.','Expert in organizing large-scale events and tailoring venues to suit corporate or social gatherings.','Providing a quiet, productive environment for study and individual work.']
        context['agent_description'] = zip(context['agents'], context['description'])
        return context


class BuildingListView(ListView):
    model = Building
    template_name = 'building/BuildingList.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['buildings'] = Building.objects.all()
        context['total_buildings'] = Building.objects.count()
        context['recent_buildings'] = Building.objects.order_by('-id')[:5]  
        return context


class BuildingDetailView(DetailView):
    model = Building
    template_name = 'building/BuildingDetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        building = self.get_object()
        context['venues'] = building.venues.all()  
        context['total_venues'] = building.venues.count()
        return context


class BuildingCreateView(CreateView):
    form_class = BuildingForm
    template_name = 'building/BuildingCreate.html'
    model = Building
    success_url = reverse_lazy('StateSpacesHub:building')

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        venue_form = VenueFormSet()
        venue_formhelper = VenueFormHelper()
        amenity_form = AmenityFormSet()  
        amenity_formhelper = AmenityFormHelper()  

        return self.render_to_response(
            self.get_context_data(
                form=form, 
                venue_form=venue_form, 
                venue_formhelper=venue_formhelper,
                amenity_form=amenity_form,  
                amenity_formhelper=amenity_formhelper  
            )
        )

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        venue_form = VenueFormSet(self.request.POST)
        amenity_form = AmenityFormSet(self.request.POST)  

        if form.is_valid() and venue_form.is_valid() and amenity_form.is_valid():  
            return self.form_valid(form, venue_form, amenity_form)  

        return self.form_invalid(form, venue_form, amenity_form)  


    def form_valid(self, form, venue_form, amenity_form):  
        self.object = form.save()
        venue_form.instance = self.object
        venue_instances = venue_form.save()
        for venue_instance in venue_instances:
            amenity_form.instance = venue_instance  
            amenity_form.save()  

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, venue_form, amenity_form):  
        return self.render_to_response(
            self.get_context_data(form=form, venue_form=venue_form, amenity_form=amenity_form)  
        )

    def get_context_data(self, **kwargs):
        ctx = super(BuildingCreateView, self).get_context_data(**kwargs)
        venue_formhelper = VenueFormHelper()
        amenity_formhelper = AmenityFormHelper()  

        if self.request.POST:
            ctx['form'] = BuildingForm(self.request.POST)
            ctx['venue_form'] = VenueFormSet(self.request.POST)
            ctx['venue_formhelper'] = venue_formhelper
            ctx['amenity_form'] = AmenityFormSet(self.request.POST)  
            ctx['amenity_formhelper'] = amenity_formhelper  
        else:
            ctx['form'] = BuildingForm()
            ctx['venue_form'] = VenueFormSet()
            ctx['venue_formhelper'] = venue_formhelper
            ctx['amenity_form'] = AmenityFormSet()  
            ctx['amenity_formhelper'] = amenity_formhelper  

        return ctx

class BuildingUpdateView(UpdateView):
    model = Building
    form_class = BuildingForm
    template_name = 'building/BuildingUpdate.html'
    success_url = reverse_lazy('StateSpacesHub:building')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['building'] = self.get_object()
        return context



class VenueListView(ListView):
    model = Venue
    template_name = 'venue/VenueList.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['venues'] = Venue.objects.all()
        context['total_venues'] = Venue.objects.count()
        context['venues_with_amenities'] = Venue.objects.filter(amenities__isnull=False).distinct()
        return context


class VenueDetailView(DetailView):
    model = Venue
    template_name = 'venue/VenueDetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        venue = self.get_object()
        context['amenities'] = venue.amenities.all()  
        context['building'] = venue.building  
        context['total_amenities'] = venue.amenities.count()
        return context


class VenueCreateView(CreateView):
    model = Venue
    form_class = VenueForm
    template_name = 'venue/VenueCreate.html'  
    success_url = reverse_lazy('StateSpacesHub:venue')

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        amenity_form = AmenityFormSet()
        amenity_formhelper = AmenityFormHelper()

        return self.render_to_response(
            self.get_context_data(form=form, amenity_form=amenity_form, amenity_formhelper=amenity_formhelper)
        )

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        amenity_form = AmenityFormSet(self.request.POST)
       
        print(form.is_valid(), amenity_form.is_valid())
        print(form.errors, amenity_form.errors)
        if form.is_valid() and amenity_form.is_valid():
            return self.form_valid(form, amenity_form)

        return self.form_invalid(form, amenity_form)

    def form_valid(self, form, amenity_form):
        self.object = form.save()
        amenity_form.instance = self.object
        print(self.request.POST.dict().items() )
        
        total_amenity_forms = int(self.request.POST.get('amenity_set-TOTAL_FORMS', 0))
        print(total_amenity_forms)
        
        for i in range(total_amenity_forms):
            amenity_form_prefix = f'amenities-{i}-'
            amenity_form_data = {
                k.replace(amenity_form_prefix, ''): v 
                for k, v in self.request.POST.dict().items() 
                if k.startswith(amenity_form_prefix)
            }
            amenity_form_data['venue'] = self.object.pk
            amenity_form_i = AmenityForm(amenity_form_data)
            if amenity_form_i.is_valid():
                amenity = amenity_form_i.save(commit=False)
                amenity.venue = self.object
                amenity.save()
            else:
                print(amenity_form_i.errors)
        return HttpResponseRedirect(self.get_success_url())
    def form_invalid(self, form, amenity_form):
        return self.render_to_response(
            self.get_context_data(form=form, amenity_form=amenity_form)
        )

    def get_context_data(self, **kwargs):
        ctx = super(VenueCreateView, self).get_context_data(**kwargs)
        amenity_formhelper = AmenityFormHelper()

        if self.request.POST:
            ctx['form'] = VenueForm(self.request.POST)
            ctx['amenity_formset'] = AmenityFormSet(self.request.POST)
            ctx['amenity_formhelper'] = amenity_formhelper
        else:
            ctx['form'] = VenueForm()
            ctx['amenity_form'] = AmenityFormSet()
            ctx['amenity_formhelper'] = amenity_formhelper

        return ctx


class VenueUpdateView(UpdateView):
    model = Venue
    form_class = VenueForm
    template_name = 'venue/VenueUpdate.html'
    success_url = reverse_lazy('StateSpacesHub:venue')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['venue'] = self.get_object()
        return context



class AmenityListView(ListView):
    model = Amenity
    template_name = 'amenity/AmenityList.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['amenities'] = Amenity.objects.all()
        context['total_amenities'] = Amenity.objects.count()
        return context


class AmenityDetailView(DetailView):
    model = Amenity
    template_name = 'amenity/AmenityDetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        amenity = self.get_object()
        context['venue'] = amenity.venue  
        context['total_venues_with_amenity'] = Venue.objects.filter(amenities=amenity).count()
        return context


class AmenityCreateView(CreateView):
    model = Amenity
    form_class = AmenityForm
    template_name = 'amenity/AmenityCreate.html'
    success_url = reverse_lazy('StateSpacesHub:amenity')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context


class AmenityUpdateView(UpdateView):
    model = Amenity
    form_class = AmenityForm
    template_name = 'amenity/AmenityUpdate.html'
    success_url = reverse_lazy('StateSpacesHub:amenity')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['amenity'] = self.get_object()
        return context




class AgentListView(ListView):
    model = Agent
    template_name = 'agent/AgentList.html'
    context_object_name = 'agents'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['agents'] = Agent.objects.all()
        context['total_agents'] = Agent.objects.count()
        return context
    
class AgentDetailView(DetailView):
    model = Agent
    template_name = 'agent/AgentDetail.html'
    context_object_name = 'agent'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agent = self.get_object()
        context['team_members'] = agent.team_members.all()  
        context['total_team_members'] = agent.team_members.count()
        return context

class AgentCreateView(CreateView):
    model = Agent
    
    
    template_name = 'agent/AgentCreate.html'
    success_url = reverse_lazy('StateSpacesHub:agent')

class AgentUpdateView(UpdateView):
    model = Agent
    
    
    template_name = 'agent/AgentUpdate.html'
    success_url = reverse_lazy('StateSpacesHub:agent')


class TeamMemberListView(ListView):
    model = TeamMember  
    template_name = 'team_member/TeamMemberList.html'
    context_object_name = 'team_members'
    

class TeamMemberDetailView(DetailView):
    model = TeamMember
    template_name = 'team_member/TeamMemberDetail.html'
    context_object_name = 'team_member'

class TeamMemberCreateView(CreateView):
    model = TeamMember
    
    template_name = 'team_member/TeamMemberCreate.html'
    success_url = reverse_lazy('StateSpacesHub:team_member')

class TeamMemberUpdateView(UpdateView):
    model = TeamMember
    
    template_name = 'team_member/TeamMemberUpdate.html'
    success_url = reverse_lazy('StateSpacesHub:team_member')


class CustomerListView(ListView):
    model = Customer  
    template_name = 'customer/CustomerList.html'
    context_object_name = 'customers'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer/CustomerDetail.html'
    context_object_name = 'customer'

class CustomerCreateView(CreateView):
    model = Customer
    
    template_name = 'customer/CustomerCreate.html'
    success_url = reverse_lazy('StateSpacesHub:customer')

class CustomerUpdateView(UpdateView):
    model = Customer
    
    template_name = 'customer/CustomerUpdate.html'
    success_url = reverse_lazy('StateSpacesHub:customer')


class ReservationListView(ListView):
    model = Reservation  
    template_name = 'reservation/ReservationList.html'
    context_object_name = 'reservations'

class ReservationDetailView(DetailView):
    model = Reservation
    template_name = 'reservation/ReservationDetail.html'
    context_object_name = 'reservation'

class ReservationCreateView(CreateView):
    model = Reservation
    
    template_name = 'reservation/ReservationCreate.html'
    success_url = reverse_lazy('StateSpacesHub:reservation')

class ReservationUpdateView(UpdateView):
    model = Reservation
    
    template_name = 'reservation/ReservationUpdate.html'
    success_url = reverse_lazy('StateSpacesHub:reservation')


class RenovationListView(ListView):
    model = Renovation  
    template_name = 'renovation/RenovationList.html'
    context_object_name = 'renovations'

class RenovationDetailView(DetailView):
    model = Renovation
    template_name = 'renovation/RenovationDetail.html'
    context_object_name = 'renovation'

class RenovationCreateView(CreateView):
    model = Renovation
    
    template_name = 'renovation/RenovationCreate.html'
    success_url = reverse_lazy('StateSpacesHub:renovation')

class RenovationUpdateView(UpdateView):
    model = Renovation
    
    template_name = 'renovation/RenovationUpdate.html'
    success_url = reverse_lazy('StateSpacesHub:renovation')