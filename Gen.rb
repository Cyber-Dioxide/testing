
system("gem install colorize")

system("clear")

require 'colorize'


def red(str)
  print "\n#{str}".colorize(:color => :red)

end

def blue(str)
  print "\n[>] #{str}".colorize(:color => :blue)
end


def random

  rang = ARGV[0].to_i

  while rang > 0
    i1 = rand(1..255)
    i2 = rand(1..255)
    i3 = rand(1..255)
    i4 = rand(1..255)
    gen = "#{i1}.#{i2}.#{i3}.#{i4}"
    blue(gen)

    file = File.new("generated.txt" , "a+")

    file.write(gen+"\n")
    rang -=1

  end

  red("Ip's Genrated successfully! ")
end

random



