def get_clean_data(source):
    data = load_data(source)
    cleanned_data = clean_data(data)
    return cleanned_data
