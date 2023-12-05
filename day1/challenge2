const numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

function getCalibration(entries){
  return entries.reduce((acc, curr) => {
    const parsed = curr.replace(/zero|one|two|three|four|five|six|seven|eight|nine/gi, (value) => numbers.indexOf(value))
            .replace(/\D/gi, "");
    acc += Number(parsed.length > 1 ? parsed[0] + parsed.slice(parsed.length - 1) : parsed[0] + parsed[0]);
    return acc;
  }, 0);
}
