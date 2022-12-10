def belongs_to_group(request, group_name):
    return request.user.groups.filter(name=group_name).exists()
