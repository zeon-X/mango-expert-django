from django.shortcuts import render, redirect, get_object_or_404
from .models import MangoExport
from .forms import MangoExportForm


# List & Search View
def mango_list(request):
    query = request.GET.get('search', '')
    mangoes = MangoExport.objects.filter(order_id__icontains=query) if query else MangoExport.objects.all()
    
    # # Debugging
    # for mango in mangoes:
    #     print(mango.order_id)  # Check the order_id for each mango
    
    return render(request, 'export_app/mango_list.html', {'mangoes': mangoes, 'query': query})

# Create View
def mango_create(request):
    if request.method == 'POST':
        form = MangoExportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mango_list')
    else:
        form = MangoExportForm()
    return render(request, 'export_app/mango_form.html', {'form': form})

# Update View
def mango_update(request, pk):
    mango = get_object_or_404(MangoExport, pk=pk)  # Retrieve the mango object
    
    if request.method == 'POST':
        form = MangoExportForm(request.POST, instance=mango)  # Pass the instance for updating
        
        if form.is_valid():  # Validate the form
            form.save()  # Save the updated mango object
            return redirect('mango_list')  # Redirect to the mango list page after successful update
        
        # form.save()  # Save the updated mango object
        # return redirect('mango_list')  # Redirect to the mango list page after successful update
    
    else:
        form = MangoExportForm(instance=mango)  # Prefill the form with the existing mango data
    
    return render(request, 'export_app/mango_update_form.html', {'form': form, 'mango': mango})


# Delete View
def mango_delete(request, pk):
    mango = get_object_or_404(MangoExport, pk=pk)
    if request.method == 'POST':
        mango.delete()
        return redirect('mango_list')
    return render(request, 'export_app/mango_confirm_delete.html', {'mango': mango})
