require 'open-uri' # consultar a la plataforma
require 'nokogiri' # formatear, parsear a html
require 'csv' # escribir y leer csv
#Keyla Fernanda Franco Hidalgo - > scraping


link = 'https://www.esportsearnings.com/games'
datosHTML = URI.open(link)
datosParseados = Nokogiri::HTML(datosHTML.read)

# separamos la pagina

#datos de la caja de juego
boxJuegos = datosParseados.css('.detail_box_game')
juegos = []
premio = []
cant_jugadores = []
cant_torneos = []
boxJuegos.css('.detail_box_game').each do |datos|
  nombreJuego = datos.css('a').inner_text
  stats = datos.css('span').inner_text 
  monto = ""
  jugadores = ""
  torneo = ""
  
  ini_monto = stats[0...stats.index(".")]
  fin_monto = stats[stats.index(".")..stats.index(".")+2]
  players = stats.index("Players")
  tournament = stats.index("Tournaments")
  
  monto =  ini_monto+ fin_monto
  jugadores = stats[stats.index(".")+3...players-1]
  torneo = stats[players+"Players".length...tournament-1]
  
  juegos.append(nombreJuego)
  premio.append(monto.gsub(/[^\d\.]/, '').to_f)
  cant_jugadores.append(jugadores.to_i)
  cant_torneos.append(torneo.to_i)
end

#datos de la lista
listajuegos=datosParseados.css('.detail_box_smooth')
listajuegos.css('.format_row').each do |data|
  nomJuego = data.css('a').inner_text
  monto = data.css('.border_right').inner_text
  jugadores = data.css('.border_left').inner_text
  players = jugadores.sub " Players", ""
  
  torneo = data.css('.detail_list_prize').inner_text
  indice = torneo.index("Tournaments")
  tournament = torneo[torneo.index("Players")...indice]
  cTorneo= tournament.sub "Players", ""
  
  juegos.append(nomJuego)
  premio.append(monto.gsub(/[^\d\.]/, '').to_f)
  cant_jugadores.append(players.to_i)
  cant_torneos.append(cTorneo.to_i)
end



CSV.open('archivos/datosTorneos.csv', 'w') do |csv|
    csv << %w"Nombre Juego, Premios, Cantidad de Jugadores, Cantidad de Torneos"
  end
flag = 0
juegos.each do |nom|
  puts flag + 1
  puts nom, premio[flag], cant_jugadores[flag], cant_torneos[flag]
  puts
 
  CSV.open('archivos/datosTorneos.csv', 'a') do |csv|
    csv << [nom, premio[flag], cant_jugadores[flag], cant_torneos[flag]]
  end
  flag += 1
end