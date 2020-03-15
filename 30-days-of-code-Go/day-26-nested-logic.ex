defmodule Solution do
  def fine(returned, due) do
    [day_returned, month_returned, year_returned] =  returned
    [day_due, month_due, year_due]  = due
    cond do
      year_returned > year_due ->
        10000
      year_returned < year_due ->
        0
      year_returned == year_due ->
        cond do
          month_returned > month_due ->
            500 * (month_returned - month_due)
          month_returned < month_due ->
            0
          month_returned == month_due ->
            cond do
               day_returned > day_due ->
                15 * (day_returned - day_due)
              true ->
                0
            end
        end
    end
  end

end

returned = IO.read(:stdio, :line)
  |> String.trim
  |> String.split
  |> Enum.map(&String.to_integer/1)
due = IO.read(:stdio, :line)
  |> String.trim
  |> String.split
  |> Enum.map(&String.to_integer/1)

IO.puts(Solution.fine(returned, due))
