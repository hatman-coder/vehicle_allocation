def serialized_data(queryset: list):
    data_list = list()

    for field in queryset:
        field["_id"] = str(field["_id"])
        data_list.append(field)

    return data_list
