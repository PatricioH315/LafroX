// Formato numerico chileno: miles con ".", decimales con ",".
const group = (s) => s.replace(/\B(?=(\d{3})+(?!\d))/g, ".");
function fmt(n, d = 0) {
  const neg = n < 0 && Math.abs(n) >= 0.5 * Math.pow(10, -d);
  const [i, f] = Math.abs(n).toFixed(d).split(".");
  return (neg ? "\u2212" : "") + group(i) + (f ? "," + f : "");
}
const pct = (x, d = 1) => fmt(x * 100, d) + " %";
const uf = (n, d = 0) => fmt(n, d) + " UF";
module.exports = { fmt, pct, uf, group };
