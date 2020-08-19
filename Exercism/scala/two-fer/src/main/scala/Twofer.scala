object Twofer {
  def twofer(name: String): String = if (name.length > 0) s"One for $name, one for me." else "One for you, one for me."
}
