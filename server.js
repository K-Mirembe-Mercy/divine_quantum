const express = require("express");
const app = express();
app.get("/", (req, res) => res.send("Divine Quantum Network – Energy in Harmony"));
app.listen(3000, () => console.log("Server running on port 3000"));
const { exec } = require("child_process");

exec("python3 quantum.py", (error, stdout, stderr) => {
    if (error) {
        console.error(error);
        return;
    }
    console.log(stdout);
});
