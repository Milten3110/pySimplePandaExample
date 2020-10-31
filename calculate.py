# Calc über ein festgelegten zeitraum (jahren) den Ertrag aus
class simpleCalc(object):
    daten = None

    def __init__(self, jahre, zins, sparrate):
        #set INIT Daten zur Berechnung
        self.daten = {
            "jahre": [0],
            "kapital": [0],
            "zinsen": [0]
        }
        zins /= 100 #auf % rechnen
        self.calc_years(jahre, zins, sparrate) #berechnet bis zum nten jahr 
    # einzahlung pro jahr
    # zins pro jahr
    # neues kapital
    # altes kapital
    # zins erträge

    # calc kapital after n years
    def calc_years(self, jahre, zins, sparrate):
        #berechnet
        #alten wert mit 4 + einzahlung für jedes jahr bis n
        for jahr in range(0,jahre):
            self.addJahr(jahr+1)
            self.calc_zins(jahr, zins)
            self.calc_newKapital(jahr, sparrate)

    def addJahr(self, jahr):
        self.daten['jahre'].append(jahr)

    def calc_zins(self, jahr, zins = 0.04):
        self.daten['zinsen'].append( float(self.daten['kapital'][jahr] * zins) )

    # calc old and new kapital
    def calc_newKapital(self, jahr, sparrate):
        self.daten['kapital'].append( float(self.daten['kapital'][jahr] + sparrate + self.daten['zinsen'][jahr+1] ) )

    def get_daten_jahre(self):
        return self.daten['jahre']
    
    def get_daten_kapital(self):
        return self.daten['kapital']
 
    def get_daten_zinsen(self):
        return self.daten['zinsen']

class complexCalc(object):
    daten = None
    def __init__(self, laufzeitJahre, einzahlungBisNJahr, zinssatz, einzahlung):
        self.daten = {
            "jahre": [0],
            "kapital": [0],
            "zinsen": [0]
        }
        zinssatz /= 100 #auf % rechnen
        self.calc_years(laufzeitJahre,zinssatz,einzahlung, einzahlungBisNJahr)

    def calc_years(self, jahre, zins, sparrate, einzahlungBisNJahr):
        #berechnet
        #alten wert mit 4 + einzahlung für jedes jahr bis n
        for jahr in range(0,jahre):
            if jahr >= einzahlungBisNJahr:
                self.addJahr(jahr+1)
                self.calc_zins(jahr, zins)
                self.calc_newKapital(jahr, 0)
            else: 
                self.addJahr(jahr+1)
                self.calc_zins(jahr, zins)
                self.calc_newKapital(jahr, sparrate)


    def addJahr(self, jahr):
        self.daten['jahre'].append(jahr)

    def calc_zins(self, jahr, zins = 0.04):
        self.daten['zinsen'].append( float(self.daten['kapital'][jahr] * zins) )

    # calc old and new kapital
    def calc_newKapital(self, jahr, sparrate):
        self.daten['kapital'].append( float(self.daten['kapital'][jahr] + sparrate + self.daten['zinsen'][jahr+1] ) )

    def get_daten_jahre(self):
        return self.daten['jahre']
    
    def get_daten_kapital(self):
        return self.daten['kapital']
 
    def get_daten_zinsen(self):
        return self.daten['zinsen']
