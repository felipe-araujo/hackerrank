defmodule Solution do
  def gdc(a, b) do
    gdc(a, b, Enum.min([a, b]))
  end

  def gdc(a, b, prev_rem) do
    [divisor, dividend] = [a, b] |> Enum.sort()
    quotient = div(dividend, divisor)
    rm = rem(dividend, divisor)

    case rm do
      0 -> {:ok, prev_rem}
      _ -> gdc(divisor, quotient, rm)
    end
  end
end

[a, b] =
  IO.read(:stdio, :line)
  |> String.trim()
  |> String.split()
  |> Enum.map(&String.to_integer/1)

{:ok, gdc} = Solution.gdc(a, b)
IO.puts(gdc)
