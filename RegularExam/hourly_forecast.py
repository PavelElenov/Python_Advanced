def forecast(*args):
    data = {}

    for item in args:
        location, weather = item
        data[location] = weather
    sunny_weather = {}
    cloudy_weather = {}
    rainy_weather = {}
    for el in data:
        if data[el] == 'Sunny':
            sunny_weather[el] = data[el]
        elif data[el] == 'Cloudy':
            cloudy_weather[el] = data[el]
        else:
            rainy_weather[el] = data[el]
    sunny_weather = dict(sorted(sunny_weather.items(), key=lambda x: x[0]))
    rainy_weather = dict(sorted(rainy_weather.items(), key=lambda x: x[0]))
    cloudy_weather = dict(sorted(cloudy_weather.items(), key=lambda x: x[0]))
    result = []
    for el in sunny_weather:
        result.append(f"{el} - {data[el]}")
    for el in cloudy_weather:
        result.append(f"{el} - {data[el]}")
    for el in rainy_weather:
        result.append(f"{el} - {data[el]}")

    return '\n'.join(result)


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

