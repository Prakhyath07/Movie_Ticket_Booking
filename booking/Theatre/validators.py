from rest_framework import serializers

min_seats = 6

def validate_min_value(value):
    if value<min_seats:
        raise serializers.ValidationError(f"Minimum number of seats in a row is {min_seats}")

def validate_min_tikcet(value):
    if value<2:
        raise serializers.ValidationError(f"Minimum number of tickets to book here is 2. for one ticket visit url in previous page")