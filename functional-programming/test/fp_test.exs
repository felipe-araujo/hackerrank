defmodule FPTest do
  use ExUnit.Case
  doctest FP

  test "greets the world" do
    assert FP.hello() == :world
  end
end
