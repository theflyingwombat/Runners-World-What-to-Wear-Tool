
# pc=partly cloudy, c=clear, r=raining, lr=light rain, s=snowing, o=overcast
conditions = 'c'
if conditions is 'o':
    name_conditions = 'overcast'
elif conditions is 'c':
    name_conditions = 'clear'
elif conditions is 'r':
    name_conditions = 'raining'
elif conditions is 'lr':
    name_conditions = 'light rain'
elif conditions is 's':
    name_conditions = 'snowing'
# m or f
gender = 'm'
if gender is 'm':
    name_gender = 'male'
elif gender is 'f':
    name_gender = 'female'

# dusk, day, dusk, night
time = 'day'

# h =hard, l = long, r=race, n=normal
intensity = 'n'
if intensity is 'l':
    name_intensity = 'long run'
elif intensity is 'h':
    name_intensity = 'hard run'
elif intensity is 'n':
    name_intensity = 'normal run'
elif intensity is 'r':
    name_intensity = 'race'

# lw = light wind, hw = heavy wind, nw = no wind
wind = 'lw'
if wind is 'lw':
    name_wind = 'light wind'
elif wind is 'hw':
    name_wind = 'heavy wind'
elif wind is 'nw':
    name_wind = 'no wind'

# c=cool, w=warm, ib = in between
feel = 'ib'
if feel is 'ib':
    name_feel = 'in between'
elif feel is 'w':
    name_feel = 'warm'
elif feel is 'c':
    name_feel = 'cool'

temp = 10

data = [conditions, gender, time, intensity, wind, feel, temp]

blocks = {
    'Head': ['winter_cap', 'hat'],
    'Face': ['sunglasses'],
    'Torso': ['heavy_jacket', 'light_jacket', 'ls', 'ss', 'singlet', 'bra'],
    'Legs': ['tights', 'capris', 'shorts'],
    'Feet': ['shoes'],
    'Sunblock': ['sunblock']}

items = {
    'winter_cap': {
        'min_temp': -20,
        'max_temp': 38,
        'title': 'Winter Cap',
        'desc': 'A warm hat that covers your ears is a must on cold days, especially windy ones, and can be one of the best steps you can take to keep warm. Merino wool, fleece, and technical-fiber options are available at specialty running stores.',
        'requirements': conditions != 'r',
        'male': 'm_head_wintercap.png',
        'female': 'f_head_wintercap.png'},

    'hat': {
        'min_temp': 38,
        'max_temp': 120,
        'title': 'Hat with Visor',
        'desc': 'A hat with a visor serves not only to keep the sun out of your eyes, but also to shield them from blowing snow and rain on the run. A lighter-colored hat helps to keep your head cool on warm days.',
        'male': 'm_head_hat.png',
        'female': 'f_head_hat.png',
        'requirements': conditions in ['pc', 'c'] and time != 'night'},

    'sunglasses': {
        'min_temp': -20,
        'max_temp': 120,
        'title': 'Sunglasses',
        'desc': 'By keeping the sun out of your eyes, a good pair of sunglasses can save you energy by allowing you to relax your face (no squinting). Though their uses are obvious on sunny summer days, they\'re also useful on bright winter days, or any other time when glare is likely to be an issue.',
        'requirements': conditions in ['pc', 'c'] and time != 'night'},

    'heavy_jacket': {
        'min_temp': -20,
        'max_temp': 19,
        'title': 'Heavy Jacket',
        'desc': 'A heavy jacket will help keep you warm on those really chilly days. If you don\'t have one, another option is layers. You\'ll get the same warmth from a sweatshirt underneath a light jacket, just be sure that your outer layer is water resistant. Use the zipper as a &quot;thermostat&quot; &ndash; zip up or down on the run, as needed, to stay comfortable.',
        'url': 'https:#www.runnersworld.com/content/jackets/'},

    'light_jacket': {
        'min_temp': 20,
        'max_temp': 40,
        'title': 'Light Jacket',
        'desc': 'A jacket, usually a polyester blend, serves to keep you warm, keep off wind, rain, and snow, and manage your perspiration. It\'s an essential piece of equipment on cold, windy and/or rainy days. Use the zipper as a &quot;thermostat&quot; &ndash; zip up or down on the run, as needed, to stay comfortable.',
        'male': 'm_torso_lightjacket.png',
        'female': 'f_torso_lightjacket.png'},

    'ls': {
        'min_temp': 40,
        'max_temp': 54,
        'title': 'Long-Sleeve Shirt',
        'desc': 'A long-sleeve shirt made of high-tech polyester will pull moisture away from your skin, keeping you from getting clammy and cold on a cooler day.',
        'male': 'm_torso_ls.png',
        'female': 'f_torso_ls.png'},

    'ss': {
        'min_temp': 54,
        'max_temp': 65,
        'title': 'Short-Sleeve Shirt',
        'desc': 'While this may look like a classic T-shirt, a runner is actually best-off with a technical fabric like CoolMax which will pull sweat away from the skin, instead of absorbing it like cotton. This added comfort, combined with sun protection, can make a technical T-shirt a great choice.',
        'male': 'm_torso_ss.png',
        'female': 'f_torso_ss.png'},

    'singlet': {
        'min_temp': 65,
        'max_temp': 120,
        'title': 'Singlet',
        'desc': 'A singlet &ndash; a loose fitting tank top &ndash; is a great choice for runners on warm days, especially in races.',
        'special': gender == 'm' and intensity == 'r' and adjusted > 35 or gender == 'f' and adjusted >= 80 and adjusted <= 85,
        'male': 'm_torso_singlet.png',
        'female': 'f_torso_singlet.png'},

    'bra': {
        'title': 'Sports Bra',
        'desc': 'For women, a sports bra is a &quot;must-have&quot; piece of equipment for running happy. If you are experiencing pain and swelling, you are most likely in the wrong bra.',
        'url': 'https:#www.runnersworld.com/content/sports/-bras',
        'requirements': gender == 'f'},

    'tights': {
        'min_temp': -20,
        'max_temp': 40,
        'title': 'Tights',
        'desc': 'The first level of insulation for your legs. &quot;Classic&quot; tights are generally a polyester and spandex blend. Looser running pants (also stretchy, but not as form-fitting as tights) are another option here. In extreme cold, tights under pants is a good layering strategy. Underwear under the tights is a good idea; just try to avoid cotton.',
        'male': 'm_legs_tights.png',
        'female': 'f_legs_tights.png'},

    'capris': {
        'min_temp': 35,
        'max_temp': 50,
        'title': 'Capri Tights',
        'desc': 'Capri tights only cover down to the mid-calf and are a great option for in-between weather. Underwear under the tights is a good idea; just try to avoid cotton.',
        'requirements': gender == 'f',
        'female': 'f_legs_capris.png'},

    'shorts': {
        'min_temp': 40,
        'max_temp': 120,
        'title': 'Shorts',
        'desc': 'The basic element of any runner\'s wardrobe. Usually a nylon or technical fiber. Briefs or underwear are optional; some runners use them, some don\'t. Just avoid cotton.',
        'male': 'm_legs_shorts.png',
        'female': 'f_legs_shorts.png'},

    'sunblock': {
        'min_temp': -20,
        'max_temp': 120,
        'title': 'Sunblock',
        'desc': 'A must for sunny days, sunblock will actually keep you cooler while preventing sunburn and reducing your risk of skin cancer. Use at least SPF-30; higher doesn\'t hurt. Also, use plenty. Applying sunblock too thinly reduces its effectiveness.',
        'requirements': conditions in ['c', 'pc'] and time == 'day',
        'url': 'https:#www.runnersworld.com/content/sunscreen/'},

    'shoes': {
        'min_temp': -20,
        'max_temp': 120,
        'title': 'Running Shoes',
        'desc': 'Choose a pair of running shoes with the cushioning and stability appropriate for your biomechanics. Or go barefoot (weather permitting, of course). If wearing shoes, a good pair of moisture-wicking running socks can help prevent blisters.',
        'male': 'm_feet_shoes.png',
        'female': 'f_feet_shoes.png'},

    'gloves': {
        'min_temp': -20,
        'max_temp': 77,
        'title': 'Gloves',
        'desc': 'When in doubt, wear gloves or mittens; if you get too warm, they\'re easy to tuck into your shorts or tights. Gloves keep your hands warm on a cold day, but mittens are an even warmer option when temperatures plunge below freezing.',
        'url': 'https:#www.runnersworld.com/content/gloves/'}}

text_values = {
    'gender': {
        'm': 'man',
        'f': 'woman'},

    'conditions': {
        'c': 'clear',
        'pc': 'partially cloudy',
        'o': 'overcast',
        'r': 'very rainy',
        'lr': 'rainy',
        's': 'snowy'},

    'wind': {
        'nw': 'no wind',
        'lw': 'light wind',
        'hw': 'heavy wind'},

    'time': {
        'dawn': 'morning',
        'day': 'day',
        'dusk': 'evening',
        'night': 'night'},

    'intensity': {
        'n': 'going for a normal run',
        'l': 'going for a long run',
        'h': 'running a hard workout',
        'r': 'running a race'},

    'feel': {
        'c': 'who likes to feel cool',
        'ib': '',
        'w': 'who likes to feel warm'}}


def makePicks():
    adjusted = newtemp
    picks = {}
    # Loop through blocks (head, torso, etc)
    for key, value in blocks.items():
        picks[key] = {}
        pick = False
        print(key)
        # Loop through possible block items (hat, visor, etc)
#        try:
        for val in value:
            # Check if conditions meet item requirements
            item = items[val]
            req_check = item.get('requirements')
            try:
                if ((item['min_temp'] or adjusted >= item['min_temp']) and (not item['max_temp'] or adjusted <= item['max_temp'])):
                    if req_check is True and item['requirements'] is True:
                        pick = item['title']
                        break
                    elif req_check is True and item['requirements'] is False:
                        print(item)
                        print(item['requirements'])
                        continue
                    elif req_check is False:
                        continue
                    else:
                        pick = item['title']
                        break

            except KeyError:
                continue
                pick = item['title']
                print('Exception: ')

                break

        picks[key] = pick
        print(pick)

        # Add on long sleeve shirt, bra if necessary
        if (key == 'Torso'):
            print(adjusted)
            print(pick)
            if (adjusted <= 40 and pick != 'Long-Sleeve Shirt'):
                print('long sleeve shirt')
                picks.update({'Shirt': 'Long-Sleeve Shirt'})
                # picks.ls = items.ls
            if (gender == 'f' and pick != 'bra'):
                picks.bra = items.bra
            if (adjusted < 47 and pick != 'Singlet'):
                picks.update({'Gloves': 'Gloves'})
                print('Gloves')
    return picks


def getAdjustedTemp(data):
    adjusted = temp
    # clear sunny day
    if (time == 'day' and conditions == 'c'):
        adjusted += 10
    # partly cloudy day
    elif (time == 'day' and conditions == 'pc'):
        adjusted += 5
    # clear, dawn or dusk
    elif ((time == 'dawn' or time == 'dusk') and conditions == 'c'):
        adjusted += 5
    # partly cloudy, dawn or dusk
    elif ((time == 'dawn' or time == 'dusk') and conditions == 'pc'):
        adjusted += 2
    # raining
    elif (conditions == 'r'):
        adjusted -= 10
    # light raining
    elif (conditions == 'lr'):
        adjusted -= 4
    # snowing
    elif (conditions == 's'):
        adjusted -= 3

    # if light wind
    if (wind == 'lw'):
        adjusted -= 5
    # if heavy wind
    elif (wind == 'hw'):
        adjusted -= 9

    # if a race
    if (intensity == 'r'):
        adjusted += 15
    # if a hard workout
    elif (intensity == 'h'):
        adjusted += 8
    # if a long run
    elif (intensity == 'l'):
        adjusted -= 5

    # if you like to feel cool, pretend temp is warmer
    if (feel == 'c'):
        adjusted += 10
    # if you like to feel warm, pretend temp is cooler
    elif (feel == 'w'):
        adjusted -= 10
    return adjusted


newtemp = getAdjustedTemp(data)
str_newtemp = str(newtemp)
print('Adjusted Temp: ' + str_newtemp + 'F\n')

the_picks = makePicks()
print('')
print('Picks:', the_picks)
deg = u'\xb0'
print('Here\'s what we recommend for a ' + name_gender + ' wanting to feel \'' + name_feel + '\' on a ' + name_intensity + ' on a ' + str(temp) + deg.encode('utf8') + 'F ' + name_conditions + ' ' + time + ' with ' + name_wind + '. As with any tool, you should use a bit of common sense with these results and adjust to personal taste. These gear picks are meant to be a guideline, not a steadfast rule.</p>')
print('')

for key, value in the_picks.items():
    if value is not False:
        print(key + ': ' + value)
