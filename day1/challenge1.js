function getCalibration(entries){
  return entries.reduce((acc, curr) => {
    const parsed = curr.replace(/\D/gi, "");
    acc += Number(parsed.length > 1 ? parsed[0] + parsed.slice(parsed.length - 1) : parsed[0] + parsed[0]);
    return acc;
  }, 0);
}
