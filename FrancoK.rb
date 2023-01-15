require 'open-uri' # consultar a la plataforma
require 'nokogiri' # formatear, parsear a html
require 'csv' # escribir y leer csv
#Keyla Fernanda Franco Hidalgo - > scraping

class Ordenar
  attr_accessor :lista, :juegos
  def initialize(lista, juegos)
    @lista = lista
    @juegos = juegos
  end
  def guardar (nomArchivo,numero)
    contador = 0
    veinteJugadores = lista.sort.reverse[...numero]
    for elem in veinteJugadores
        ind= veinteJugadores.index(elem)
        titulo= juegos[ind]
        contador+=1
        juegos.delete_at(ind)
        CSV.open("archivos/#{nomArchivo}.csv", 'a') do |csv|
          csv << [titulo, elem]
        end
    end
  end
  
end



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
    csv << %w"Nombre  Premios Cantidad_Jugadores Cantidad_Torneos"
end
CSV.open('archivos/veinteJugadores.csv', 'w') do |csv|
  csv << %w"Nombre Cant_Jugadores"
end
CSV.open('archivos/diezTorneos.csv', 'w') do |csv|
  csv << %w"Nombre Cant_Torneos"
end
CSV.open('archivos/porcentajeCOD.csv', 'w') do |csv|
  csv << %w"Nombre premioDado totalPremiosCOD PorcentajeGanado"
end


#Guardar datos
flag = 0
juegos.each do |nom|
  puts nom, premio[flag], cant_jugadores[flag], cant_torneos[flag]
  puts
 
  CSV.open('archivos/datosTorneos.csv', 'a') do |csv|
    csv << [nom, premio[flag], cant_jugadores[flag], cant_torneos[flag]]
  end
  flag += 1
end

# 20 juegos con más 'pro-players'
best20 = Ordenar.new(cant_jugadores, juegos)
best20.guardar("veinteJugadores", 20)
#10 juegos con mejor promedio de premios por torneo
best10 = Ordenar.new(cant_torneos, juegos)
best10.guardar("diezTorneos", 10)
#distribución de los premios entregados por cada franquicia de Call of Duty
total = 0
file = CSV.open('archivos/datosTorneos.csv').read
file.delete_at(0)
file.each do |item|
  if item[0].include?('Call of Duty')
    total += item[1].to_f
  end
end
file.each do |item|
  if item[0].include?('Call of Duty')
    porcentaje = (item[1].to_f/total) * 100
    CSV.open('archivos/porcentajeCOD.csv', 'a') do |csv|
      csv << [item[0], item[1].to_f, total, porcentaje.truncate(2)]
    end
  end
end

    
