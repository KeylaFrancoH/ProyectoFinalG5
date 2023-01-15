require 'open-uri' #consultar a la plataforma
require 'nokogiri' #formatear, parsear a html
require 'csv' #escribir y leer csv

urls = ['https://www.imdb.com/search/title/?title_type=video_game&release_date=2021-01-01,2021-12-31&sort=num_votes,desc&ref_=adv_prv', 'https://www.imdb.com/search/title/?title_type=video_game&release_date=2022-01-01,2022-12-31&sort=num_votes,desc&ref_=adv_prv']


class Game
  attr_accessor :name, :genres, :year, :directors, :resume, :votes, :stars, :rating
  def initialize(name, genres, year, directors, resume, votes, stars, rating)
    @name = name
    @directors = directors
    @stars = stars
    @genres = genres
    @year = year
    @votes = votes
    @resume = resume
    @rating = rating
  end

  def save_data
    CSV.open('archivos/games.csv', 'a') do |csv|
      csv << [@name, @genres, @year, @directors, @resume, @votes, @stars, @rating]
    end
  end

end


urls.each do |url|
  data_html = URI.open(url)
  data = data_html.read
  parsed_content = Nokogiri::HTML(data)
  game_list = parsed_content.css('.lister-list')
  game_list.css('.lister-item').each do |post|
    name = post.css('.lister-item-content').css('.lister-item-header').css('a').inner_text
    genres = post.css('.genre').inner_text
    year = post.css('.lister-item-content').css('.lister-item-year').inner_text.split(' ')[0][1..]
    info = post.css('.lister-item-content').css('p:nth-child(5)').inner_text
    resume = post.css('.lister-item-content').css('.text-muted').css('p:nth-child(4)').inner_text
    votes = post.css('.lister-item-content').css('.sort-num_votes-visible').css('span:nth-child(2)').attr('data-value')
    rating = post.css('.lister-item-content').css('.ratings-imdb-rating').attr('data-value')
    if info.include? 'Director'  and info.include?'Star'
      directors = info.split('|')[0].strip()
      stars = info.split('|')[1].strip()
    elsif info.include? 'Director'  and not info.include? 'Star'
      directors = info.chomp('Director').strip()
      stars = 'None'
    elsif not info.include? 'Director' and info.include?'Star'
      directors = 'None'
      stars = info.chomp('Star').strip()
    else
      directors = 'None'
      stars = 'None'
    end
    game1 = Game.new(name, genres, year, directors, resume, votes, stars, rating)
    game1.save_data
  end
end
