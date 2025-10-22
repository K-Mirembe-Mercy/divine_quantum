const express = require("express");
const app = express();
app.get("/", (req, res) => res.send("Divine Quantum Network – Energy in Harmony"));
app.listen(3000, () => console.log("Server running on port 3000"));
