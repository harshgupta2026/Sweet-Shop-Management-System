import express from "express";
import cors from "cors";

const app = express();
app.use(cors());
app.use(express.json());

let sweets = [
  { id: 1, name: "Kaju Katli", category: "Dry Fruit", price: 500 },
  { id: 2, name: "Gulab Jamun", category: "Milk", price: 300 },
  { id: 3, name: "Rasgulla", category: "Milk", price: 250 }
];

// GET
app.get("/api/sweets", (req, res) => {
  res.json(sweets);
});

// POST
app.post("/api/sweets", (req, res) => {
  const newSweet = { id: Date.now(), ...req.body };
  sweets.push(newSweet);
  res.json(newSweet);
});

// DELETE
app.delete("/api/sweets/:id", (req, res) => {
  sweets = sweets.filter(s => s.id != req.params.id);
  res.json({ success: true });
});

app.listen(8000, () => {
  console.log("Backend running on http://localhost:8000");
});
