import numpy as np
import pandas as pd



# Neighborhood to borough

manhattan = ["Civic Center","Beekman","North New York","Two Bridges","Fort George","West Harlem","Nolita","Upper Carnegie Hill","Little Italy","Manhattan","Central Park South","Fulton/Seaport","Hamilton Heights","Sutton Place","Turtle Bay","Midtown South","Noho","NoMad","Lenox Hill","Yorkville","Flatiron","Midtown","Soho","West Chelsea","Hudson Heights","Central Harlem","Stuyvesant Town/PCV","Alphabet City","Battery Park City","Carnegie Hill","Chelsea","Chinatown","East Harlem","East Village","Financial District","Flatiron District","Gramercy Park","Greenwich Village","Harlem","Hell's Kitchen/Clinton","Inwood","Kips Bay","Lincoln Square","Lower East Side","Manhattan Valley","Midtown East","Midtown West","Morningside Heights","Murray Hill","NoLita/Little Italy","Roosevelt Island","SoHo","Tribeca","Upper East Side","Upper West Side","Washington Heights","West Village"]
bronx = ["Morrisania","Highbridge","Crotona Park East","Park Hill","Mt. Hope","Marble Hill","Concourse","Westchester Village","Spuyten Duyvil","Baychester/Co-op City","Bedford Park","Belmont","Bronxdale","Castle Hill","City Island","Concourse Village/Grand Concourse/Morrisania","Country Club","Fieldston","Fordham","Hunts Point","Kingsbridge","Kingsbridge Heights","Melrose","Morris Heights","Morris Park","Mott Haven","Parkchester","Pelham Bay","Pelham Gardens","Pelham Parkway","Port Morris","Riverdale","Soundview","Throgs Neck","Tremont","University Heights","Wakefield","Williamsbridge","Woodlawn"]
queens = ["Glen Oaks Village","Clearview","Glen Oaks Village","Queensboro Hill","Murray Hill (Queens)","Pomonok","Kew Gardens Hills","East Flushing","Bay Terrace (Queens)","North Corona","Hunters Point","Arverne","Astoria","Bayside","Beechhurst","Belle Harbor/Neponsit","Bellerose","Briarwood","Broad Channel","Cambria Heights","College Point","Corona","Douglaston","East Elmhurst","Elmhurst","Far Rockaway","Floral Park","Flushing","Forest Hills","Fresh Meadows","Glen Oaks","Glendale","Hillcrest","Hollis","Hollis Hills","Howard Beach","Jackson Heights","Jamaica","Jamaica Estates","Jamaica Hills","Kew Gardens","Laurelton","Little Neck","Long Island City","Maspeth","Middle Village","Oakland Gardens","Ozone Park","Queens Village","Rego Park","Richmond Hill","Ridgewood","Rockaway Park","Rosedale","South Jamaica","South Ozone Park","Springfield Gardens","St. Albans","Sunnyside","Whitestone","Woodhaven","Woodside"]
brooklyn = ["Farragut","City Line","Wingate","Homecrest","Weeksville","Greenwood","Columbia St Waterfront District","Fort Hamilton","Ditmas Park","Fort Greene","DUMBO","Vinegar Hill","Kensington", "Brooklyn","Prospect Park South","East Williamsburg","Ocean Hill","Northeast Flatbush","Prospect Lefferts Gardens","Clinton Hill","Ocean Parkway","Stuyvesant Heights","Bath Beach","Bay Ridge","Bedford-Stuyvesant","Bensonhurst","Bergen Beach","Boerum Hill","Borough Park","Brighton Beach","Brooklyn Heights","Brownsville","Bushwick","Canarsie","Carroll Gardens","Cobble Hill","Coney Island","Crown Heights","Cypress Hills","Downtown Brooklyn","Dumbo/Vinegar Hill","Dyker Heights","East New York","Flatbush","Flatlands","Fort Greene/Clinton Hill","Gerritsen Beach","Gowanus","Gravesend","Greenpoint","Greenwood Heights","Manhattan Beach","Marine Park","Midwood","Mill Basin","Park Slope","Prospect Heights","Prospect Park South/Kensington","Red Hook","Sea Gate","Sheepshead Bay","Sunset Park","Williamsburg","Windsor Terrace"]
staten_island = ["Elm Park","Saint George","Princes Bay","Annadale","Arden Heights","Arrochar","Bay Street","Bulls Head","Castleton Corners","Charleston","Clifton","Dongan Hills","Eltingville","Emerson Hill","Graniteville","Grant City","Grasmere/Concord","Great Kills","Grymes Hill","Huguenot","Livingston","Manor Heights","Mariners Harbor","Midland Beach","New Brighton","New Dorp/New Dorp Beach","New Springville","Oakwood","Pleasant Plains","Port Richmond","Prince's Bay","Richmondtown","Rosebank","Rossville","Shore Acres","Silver Lake","South Beach","St. George","Stapleton","Sunnyside","Todt Hill","Tompkinsville","Tottenville","Travis","West New Brighton","Westerleigh","Willowbrook","Woodrow"]

def get_boro(place):
    if (place in manhattan):
        return "Manhattan"
    if (place in bronx):
        return "Bronx"
    if (place in queens):
        return "Queens"
    if (place in brooklyn):
        return "Brooklyn"
    if (place in staten_island):
        return "Staten Island"
    
# df['boro'] = df['where'].map(get_boro)

# Remove random stuff
# newdf = newdf.drop(newdf[newdf['boro']==1].query('price > 0').sample(frac=.2).index)