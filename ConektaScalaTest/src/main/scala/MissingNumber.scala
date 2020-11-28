import NaturalNumbers._

import scala.util.control.Breaks._

object MissingNumber {

  def main(args: Array[String]): Unit = {

    try {
      //Take the value to extract from the args
      var numberExtract = args(0).toInt

      //Validate if the number is in the range
      if (numberExtract >= 1 & numberExtract <= 100) {

        //Get the new List without the value to extract
        var newNumberList = extractNumber(fillNumbers(), numberExtract)

        var missingNumber = 0
        //Iterating the list to verify the missing number
        breakable {
          for (i <- 1 to 100) {
            if (newNumberList(i - 1) != i) {
              missingNumber = i
              println("El numero faltante es " + missingNumber)
              break
            }
          }
        }
      }
      else {
        println("El valor a extraer no esta en el rango de 1 a 100")
      }
    } catch {
      case x: NumberFormatException => {
        // exception is found
        println("El valor ingresado no es numero")

      }
    }

  }


}
