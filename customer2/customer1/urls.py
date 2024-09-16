
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),  # localhost:8000/user/
]

# PG booking system:
# Finding a PG that is available and meets your needs.: There are many PGs available, but it can be difficult to find one that is available when you need it and that meets your needs in terms of location, amenities, and price.
# Dealing with unresponsive or unhelpful landlords.: Some landlords are not very responsive to inquiries or requests, which can make it difficult to book a PG.
# Having to pay a security deposit.: Most PGs require a security deposit, which can be a significant amount of money.

# Ticket management system:
# Not being able to get in touch with customer support when you need help.: It can be frustrating if you are having a problem with a product and you cannot get in touch with customer support to get help.
# Having to wait a long time for a response from customer support.: Even if you are able to get in touch with customer support, it can take a long time to get a response.
# Not being able to resolve your issue.: Sometimes, customer support is unable to resolve your issue, which can be very frustrating.

# Hotel seat and food reservation:
# Not being able to find a hotel that has available seats and food.: It can be difficult to find a hotel that has available seats and food, especially if you are booking at the last minute.
# Having to pay a deposit.: Most hotels require a deposit, which can be a significant amount of money.
# Not being able to cancel your reservation without penalty.: Many hotels have strict cancellation policies, which means that you may have to pay a fee if you need to cancel your reservation.

# Event management:
# Not being able to find events that you are interested in.: There are many events happening all the time, but it can be difficult to find events that you are interested in.
# Having to pay for events.: Many events are expensive, which can make it difficult to attend all of the events that you are interested in.
# Not being able to get tickets to events.: Some events sell out quickly, which can make it difficult to get tickets.

# Automatic parking management:
# Not being able to find a parking spot.: It can be difficult to find a parking spot, especially in crowded areas.
# Having to pay for parking.: Parking can be expensive, especially in crowded areas.
# Getting a parking ticket.: It is easy to get a parking ticket if you do not park in the correct spot or if you do not pay for parking.