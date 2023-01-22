require 'open-uri' # consultar a la plataforma
require 'nokogiri' # formatear, parsear a html
require 'csv' # escribir y leer csv

# nom, id[flag], paises[flag + 1], fortuna[flag + 1], juegos[flag + 1]
class Jugador
  attr_accessor :nombre, :id, :pais, :fortuna, :juego
  def initialize(nombre, id, pais, fortuna, juego)
    @nombre = nombre
    @id = id
    @pais = pais
    @fortuna = fortuna
    @juego = juego
  end

  def guardar
    CSV.open('informacion.csv', 'a') do |csv|
      csv << [@nombre, @id, @pais, @fortuna, @juego]
    end
  end
end
link = 'https://www.esportsearnings.com/players'
datosHTML = URI.open(link)
datosParseados = Nokogiri::HTML(datosHTML.read)
separamos la pagina
listaJuegos = datosParseados.css('.detail_list_box')
cont = 0
id = []
nombres = []
paises = []
fortuna = []
juegos = []
listaJuegos.css('.format_row').each do |post|
  pais = post.css('.detail_list_player').css('img').attr('title')
  paises.append(pais)
  post.css('.detail_list_player').each do |player|
    cont += 1
    id.append(player.inner_text) if cont.odd?
    nombres.append(player.inner_text) if cont.even?
  end
  total = post.css('.border_right').inner_text
  juego = post.css('.border_left').inner_text
  fortuna.append(total)
  juegos.append(juego)
end
flag = 0
nombres.each do |nom|
  jugador = Jugador.new(nom, id[flag], paises[flag + 1], fortuna[flag + 1], juegos[flag + 1])
  jugador.guardar
  flag += 1
end
des = 0
CSV.foreach('informacion.csv') do |row|
  puts des + 1
  puts row[0]
  puts row[1]
  puts row[2]
  puts row[3]
  puts row[4]
  CSV.open('topGanancias.csv', 'a') do |csv|
    csv << [row[0], row[1], row[2], row[3], row[4]]
  end
  des += 1
  break if des == 10
end
juegos = []
ganancias = []
CSV.foreach('informacion.csv') do |row|
  valor = row[3].split('$')
  ganancia = valor[1].delete(',').to_f.round(1)
  juego = row[4]
  if juegos.include? juego
    ind = juegos.index(juego)
    ganancias[ind] = ganancias[ind].round(1) + ganancia.round(1)
  else
    juegos.append(juego)
    ganancias.append(ganancia.round(1))
  end
end

juegos.each do |elem|
  ind = juegos.index(elem)
  ganancia = ganancias[ind]
  CSV.open('topGananciasxJuegos.csv', 'a') do |csv|
    csv << [elem, ganancia]
  end
end
paises = []
cant = []
CSV.foreach('informacion.csv') do |row|
  pais = row[2]
  if paises.include? pais
    ind = paises.index(pais)
    cant[ind] += 1
  else
    paises.append(pais)
    cant.append(1)
  end
end
paises.each do |elem|
  ind = paises.index(elem)
  cantidad = cant[ind]
  CSV.open('toppaises.csv', 'a') do |csv|
    csv << [elem, cantidad]
  end
end
