# Your code here
def convert_temp(temperature, input_scale: , output_scale: 'celsius')
    if input_scale == output_scale then
        return temperature
    end
    if  not ['celsius', 'fahrenheit', 'kelvin'].include?(input_scale)
        return temperature
    end
    
    if not ['celsius', 'fahrenheit', 'kelvin'].include?(output_scale)
        return temperature
    end
    
    case input_scale
        when 'celsius'
            case output_scale
                when 'kelvin'
                    temperature + 273.15
                when 'fahrenheit'
                    (temperature * 1.8) + 32                
            end
        when 'kelvin'
            case output_scale
                when 'celsius'
                    temperature - 273.15
                when 'fahrenheit'
                    (temperature - 273.15)*(9.0/5) + 32                
            end
        when 'fahrenheit'
            case output_scale
                when 'celsius'
                    (temperature - 32)*(5.0/9)
                when 'kelvin'
                    (temperature - 32)*(5.0/9) + 273.15            
            end        
    end
end

puts 'should be 273.15'
puts convert_temp(0, input_scale: 'celsius', output_scale: 'kelvin')
puts
puts 'should be 32.0'
puts convert_temp(0, input_scale: 'celsius', output_scale: 'fahrenheit')
puts 
puts 'should be 93.33'
puts convert_temp(200, input_scale: 'fahrenheit', output_scale: 'celsius')