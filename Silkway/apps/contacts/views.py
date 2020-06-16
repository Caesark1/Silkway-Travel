from django.shortcuts import render
from django.views.generic import ListView

def view_map(request):
    # mapbox_access_token = "pk.eyJ1Ijoic2t5Y3JvdyIsImEiOiJja2JnZjNtY2EwbDJyMnltejdsMnI4bm43In0.bGtXiz0gFPjHizDoqqTvxw"
    return render(request, "contacts/contact.html" )
    

# {"mapbox_access_token":mapbox_access_token}
