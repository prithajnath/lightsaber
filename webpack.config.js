module.exports = {
  entry: "./index.js",
  mode: process.env.DEBUG == 1 ? "development" : "production",
  output: {
    filename: "content.js",
  },
};
