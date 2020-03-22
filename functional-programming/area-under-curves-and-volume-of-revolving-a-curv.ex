defmodule Solution do
  def calc(a, b, x) do
    Enum.zip(a, b)
      |> Enum.map(fn {ai, bi} -> ai*(:math.pow(x, bi)) end)
      |> Enum.sum
  end

  def area(l, r, f) do
    step = 0.001
    nsteps = Kernel.trunc((r-l)/step)+1

    dS = fn xi -> (step)*(f.(xi)+f.(xi+step))/2 end

    Stream.iterate({step * f.(l), l},
          fn {_dSi, xi} -> {dS.(xi), xi+step} end)
      |> Enum.take(nsteps)
      |> Enum.map(fn {dSi, _xi} -> dSi end)
      |> Enum.sum
  end

  def volume(l, r, f) do
    step = 0.001
    nsteps = Kernel.trunc((r-l)/step)+1

    dV = fn xi -> :math.pi*(step)*:math.pow((f.(xi)+f.(xi+step))/2, 2) end

    Stream.iterate({step * f.(l), l},
          fn {_dVi, xi} -> {dV.(xi), xi+step} end)
      |> Enum.take(nsteps)
      |> Enum.map(fn {dVi, _xi} -> dVi end)
      |> Enum.sum
  end
end

a = IO.read(:stdio, :line)
  |> String.trim
  |> String.split
  |> Enum.map(&String.to_integer/1)

b = IO.read(:stdio, :line)
  |> String.trim
  |> String.split
  |> Enum.map(&String.to_integer/1)

[l, r] = IO.read(:stdio, :line)
  |> String.trim
  |> String.split
  |> Enum.map(&String.to_integer/1)

#IO.puts("a, b = ")
#IO.inspect(a)
#IO.inspect(b)
#IO.puts("l= #{l}, r=#{r}")

f = fn x -> Solution.calc(a, b, x) end

Solution.area(l, r, f)
  |> IO.puts
Solution.volume(l, r, f)
  |> IO.puts
