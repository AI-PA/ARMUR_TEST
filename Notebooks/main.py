def Consulta_API(Longitud_Inicio,Latitud_Inicio,Longitud_Final,Latitud_Final,Consulta=None):
    try: 
        r = requests.get(f"""http://router.project-osrm.org/route/v1/car/{Longitud_Inicio},{Latitud_Inicio};{Longitud_Final},{Latitud_Final}?overview=false""")
        r = json.loads(r.content)["routes"][0]
        if Consulta =="T":
            r = datetime.timedelta(seconds=r['duration'])
            return str(r)
        elif Consulta =='D':
            return r['distance']
        else:
            return r
    except: 
        return
