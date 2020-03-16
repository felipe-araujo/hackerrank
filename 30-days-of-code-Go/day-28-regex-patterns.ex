defmodule Solution do
  def email_matches?(email) do
    String.match?(email, ~r/.+@gmail.com$/)
  end
end

size = IO.read(:stdio, :line)
  |> String.trim
  |> String.to_integer

Enum.to_list(0..size-1)
  |> Enum.map(fn _ -> IO.read(:stdio, :line) end)
  |> Enum.map(&String.trim/1)
  |> Enum.map(&String.split/1)
  |> Enum.filter(fn [_, email] -> Solution.email_matches?(email) end)
  |> Enum.sort_by(fn [name, _] -> name end)
  |> Enum.each(fn [name, _] -> IO.puts(name) end)
