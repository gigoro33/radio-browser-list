import requests
r = requests.get('http://nl1.api.radio-browser.info/json/stations')
if r.status_code == 200:
    data = r.json()
    # Nombre del archivo que se va a crear
    fileName = "radio_browser.m3u"

    # Crear y escribir en el archivo
    with open(fileName, 'w') as file:
        file.write("#EXTM3U\n")

    for item in data:
        # Crear y escribir en el archivo
        with open(fileName, 'a') as file:
            # tags_list = item["tags"].split(",")
            # tags_string = ""
            # if item["tags"].strip():
            #     for tag in tags_list:
            #         tags_string += f"#EXTGRP: {tag.strip()}\n"
            file.write('\n#EXTINF:1 radio="true"'
                + f' tvg-logo="{item["favicon"].strip()}"'
                + f",{item['name'].strip()}\n"
                # + tags_string
                + f"{item['url_resolved']}\n"
            )
