object NaturalNumbers {
  //Method that removes an specific value from the list
  def extractNumber(numberList: List[Int], value: Int): List[Int] = numberList match {
    case `value` :: tail => tail
    case x :: tail => x :: extractNumber(tail, value)
    case _ => Nil
  }

  //Method that creates the natural Number List
  def fillNumbers(): List[Int] = {
    var naturalNumbers = List.range(1, 101)
    return naturalNumbers
  }
}
