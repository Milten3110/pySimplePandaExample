import pandas as pd
from matplotlib import pyplot as plt
import calculate


#example
#simple
	#finanzmappe = calculate.simpleCalc(Laufzeit,Zinssatz,Jahressparrate)
	#finanzmappe = calculate.simpleCalc(20,4,500)
#complex
	#finanzmappe = calculate.complexCalc(Laufzeit,JahreDieEingezahltWerden,Zinssatz,Sparrate)
	#finanzmappe = calculate.complexCalc(40,10,4,500)



#simple
#jahre 		= 10 // die insgesamt eingezahlt werden
#zinssatz 	= 4 //Jahreszins für den gesamten einzahl Zahlraum
#sparrate 	= 500 //Jährlich
#finanzmappe = calculate.simpleCalc(jahre,zinssatz,sparrate)

#complex
#laufzeit			= 40  	//Berechnung bis N Jahre
#jahreZumEinzahlen 	= 10 	//Bis zu welchen Jahr wird die Sparrate eingezahlt und dannach nur mit Zinseszins gerechnet
#zinssatz 			= 4		//Jahreszins für den gesamten einzahl Zahlraum
#sparrate 			= 500	//Jährlich
#finanzmappe = calculate.complexCalc(laufzeit,jahreZumEinzahlen,zinssatz,sparrate)


jahre = finanzmappe.get_daten_jahre()
kapital = finanzmappe.get_daten_kapital()
zinsen = finanzmappe.get_daten_zinsen()


#anzeige
plt.plot(jahre, kapital, jahre, zinsen)
plt.xlabel("Jahre")
plt.ylabel("Kapital")
plt.legend(["Kapital", "Zinsen"])

print("Gesamt Kapital nach " , jahre[len(jahre)-1], " Jahren, folgendes : " , kapital[len(kapital)-1] , " €")
plt.show()