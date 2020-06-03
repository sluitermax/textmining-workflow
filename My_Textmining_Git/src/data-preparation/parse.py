import json

f = open('../../gen/data-preparation/temp/Fortniteastronomicalevent.json','r', encoding='utf-8')

con = f.readlines()

outfile = open('../../gen/data-preparation/temp/parsed-data.csv', 'w', encoding = 'utf-8')

outfile.write('Screenname\tcreated_at\tlocation\ttext\n')

cnt = 0
for line in con:
    #if (len(line)<=5): continue

    cnt+=1
    obj = json.loads(line.replace('\n',''))

    location = str(obj.get('user').get('location'))
    if (str(location)=='Atlanta'): location = 'USA'
    if (str(location)=='Austin'): location = 'USA'
    if (str(location)=='Baltimore'): location = 'USA'
    if (str(location)=='Boston'): location = 'USA'
    if (str(location)=='Brooklyn'): location = 'USA'
    if (str(location)=='California'): location = 'USA'
    if (str(location)=='Camden'): location = 'USA'
    if (str(location)=='Catoosa'): location = 'USA'
    if (str(location)=='Chicago'): location = 'USA'
    if (str(location)=='Cleveland'): location = 'USA'
    if (str(location)=='Columbus'): location = 'USA'
    if (str(location)=='Dallas'): location = 'USA'
    if (str(location)=='Danville'): location = 'USA'
    if (str(location)=='Florida'): location = 'USA'
    if (str(location)=='Hollywood'): location = 'USA'
    if (str(location)=='Houston'): location = 'USA'
    if (str(location)=='Illinois'): location = 'USA'
    if (str(location)=='Kentucky'): location = 'USA'
    if (str(location)=='Las Vegas'): location = 'USA'
    if (str(location)=='Los Angeles'): location = 'USA'
    if (str(location)=='Louisville'): location = 'USA'
    if (str(location)=='Manhattan'): location = 'USA'
    if (str(location)=='Maryland'): location = 'USA'
    if (str(location)=='Marysville'): location = 'USA'
    if (str(location)=='Miami'): location = 'USA'
    if (str(location)=='New Jersey'): location = 'USA'
    if (str(location)=='New York'): location = 'USA'
    if (str(location)=='North America'): location = 'USA'
    if (str(location)=='North Carolina'): location = 'USA'
    if (str(location)=='NYC'): location = 'USA'
    if (str(location)=='Oakland'): location = 'USA'
    if (str(location)=='Orlando'): location = 'USA'
    if (str(location)=='Philadelphia'): location = 'USA'
    if (str(location)=='Queens'): location = 'USA'
    if (str(location)=='San Diego'): location = 'USA'
    if (str(location)=='San Francisco'): location = 'USA'
    if (str(location)=='South Carolina'): location = 'USA'
    if (str(location)=='South Dakota'): location = 'USA'
    if (str(location)=='Tampa'): location = 'USA'
    if (str(location)=='Texas'): location = 'USA'
    if (str(location)=='U.S. '): location = 'USA'
    if (str(location)=='United States'): location = 'USA'
    if (str(location)=='United states'): location = 'USA'
    if (str(location)=='USA'): location = 'USA'
    if (str(location)=='Utah'): location = 'USA'
    if (str(location)=='Virginia'): location = 'USA'
    if (str(location)=='Wellington'): location = 'USA'
    if (str(location)=='Wisconsin'): location = 'USA'

    if (str(location)=='Albania'): location = 'Europe'
    if (str(location)=='Armenia'): location = 'Europe'
    if (str(location)=='Austria'): location = 'Europe'
    if (str(location)=='Azerbaijan'): location = 'Europe'
    if (str(location)=='Belgium'): location = 'Europe'
    if (str(location)=='Bosnia and Herzegovina'): location = 'Europe'
    if (str(location)=='Bulgaria'): location = 'Europe'
    if (str(location)=='Croatia'): location = 'Europe'
    if (str(location)=='Cyprus'): location = 'Europe'
    if (str(location)=='Czechia'): location = 'Europe'
    if (str(location)=='Denmark'): location = 'Europe'
    if (str(location)=='Estonia'): location = 'Europe'
    if (str(location)=='Finland'): location = 'Europe'
    if (str(location)=='France'): location = 'Europe'
    if (str(location)=='Georgia'): location = 'Europe'
    if (str(location)=='Germany'): location = 'Europe'
    if (str(location)=='Greece'): location = 'Europe'
    if (str(location)=='Hungary'): location = 'Europe'
    if (str(location)=='Iceland'): location = 'Europe'
    if (str(location)=='Ireland'): location = 'Europe'
    if (str(location)=='Italy'): location = 'Europe'
    if (str(location)=='Kazakhstan'): location = 'Europe'
    if (str(location)=='Kosovo'): location = 'Europe'
    if (str(location)=='Latvia'): location = 'Europe'
    if (str(location)=='Liechtenstein'): location = 'Europe'
    if (str(location)=='Lithuania'): location = 'Europe'
    if (str(location)=='Luxembourg'): location = 'Europe'
    if (str(location)=='Malta'): location = 'Europe'
    if (str(location)=='Molova'): location = 'Europe'
    if (str(location)=='Monaco'): location = 'Europe'
    if (str(location)=='Montenegro'): location = 'Europe'
    if (str(location)=='Netherlands'): location = 'Europe'
    if (str(location)=='North Macedonia'): location = 'Europe'
    if (str(location)=='Macedonia'): location = 'Europe'
    if (str(location)=='Norway'): location = 'Europe'
    if (str(location)=='Poland'): location = 'Europe'
    if (str(location)=='Portugal'): location = 'Europe'
    if (str(location)=='Romania'): location = 'Europe'
    if (str(location)=='Russia'): location = 'Europe'
    if (str(location)=='San Marino'): location = 'Europe'
    if (str(location)=='Serbia'): location = 'Europe'
    if (str(location)=='Slovakia'): location = 'Europe'
    if (str(location)=='Slovenia'): location = 'Europe'
    if (str(location)=='Spain'): location = 'Europe'
    if (str(location)=='Sweden'): location = 'Europe'
    if (str(location)=='Switzerland'): location = 'Europe'
    if (str(location)=='Turkey'): location = 'Europe'
    if (str(location)=='Ukraine'): location = 'Europe'
    if (str(location)=='United Kingdom'): location = 'Europe'
    if (str(location)=='UK'): location = 'Europe'
    if (str(location)=='Vatican City'): location = 'Europe'

    text = obj.get('text')
    text = text.replace('\t', '').replace('\n', '')

    outfile.write(obj.get('user').get('screen_name')+'\t'+obj.get('created_at')+'\t'+location+'\t'+text+'\n')
    #if (cnt>1000): break

print('done.')
