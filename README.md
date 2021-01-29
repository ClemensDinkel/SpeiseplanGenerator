# SpeiseplanGenerator

Version 1.0 SpeiseplanGenerator

Bereits implementierte Funktionen:
  - Generiere einen zufällig zusammengestellten Speiseplan für die Woche aus einer Liste an Gerichten. Derzeit landen die Vorschläge als txt-Datei auf deinem Desktop.
    Du kannst dabei über die kommandozeile bestimmen:
      - wie viele Vorschläge erstellt werden
      - wie oft verschiedene Typen an Gerichten im Plan enthalten sollen (z.B. vegetarisch) und wie lang deren Kochdauer sein soll.
  - Füge ein neues Gericht deiner Liste hinzu. Du kannst dabei über die kommandozeile bestimmen:
      - wie das Gericht heißt (Duplikate werden nicht akzeptiert)
      - welchem Typ das Gericht zugeordnet wird (fleisch, vegetarisch ...)
      - wie lange die Zubereitungszeit für das Gericht ist

Angedachte Funktionen:
   - Generiere...
       - Du kannst feste Tage festlegen, an denen nur ein bestimmter Typ Essen vorgeschlagen wird (z.B. freitags nur fisch)
        - Du kannst festlegen, dass ein Typ an Gerichten auch für einen anderen Typ ausgegeben werden kann (z.B. Suess kann auch bei vegetarisch ausgegeben werden)
   - Füge ...
       - Du kannst einem Gericht mehrere Typen zuweisen (z.B. Pfannkuchen kann sowohl suess, vegetarisch oder auch mit Fleisch zubereitet werden)
       - Mögliche Beilagen hinzufügen, die wenn gegeben ebenfalls zufällig vorgeschlagen werden
   - Du kannst dir deine Liste anzeigen lassen. Mit jedem neuen Eintrag wird deine Liste automatisch sortiert
   - Du kannst Listen importieren und mit Freunden austauschen
   - Du kannst Rankings für Gerichte vergeben. Damit kannst du die Wahrscheinlichkeit, dass ein bestimmtes Gericht ausgewählt wird, erhöhen oder verringern.
       - Du kannst einstellen, dass ein Gericht, das du erst gegessen hast, ein geringeres Ranking erhält.
         Es "erholt" sich aber mit der Zeit wieder auf sein Ursprunglevel.
   - Deine Eingaben erfolgen nicht mehr über die kommandozeile, sondern über ein GUI
   - Dein SpeisplanGenerator erstellt dir eine Einkaufsliste
