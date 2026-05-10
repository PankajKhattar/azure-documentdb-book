const { MongoClient } = require("mongodb");

async function processOrder(order) {

  console.log("Processing order:", order._id);

  if (order.amount > 1000) {
    console.log("High-value order detected");
  }

  if (order.status === "completed") {
    console.log("Order completed event received");
  }
}

async function run() {

  const uri = "mongodb://localhost:27017";

  const client = new MongoClient(uri);

  try {

    await client.connect();

    console.log("Connected to Azure DocumentDB");

    const db = client.db("shop");
    const collection = db.collection("orders");

    const changeStream = collection.watch();

    console.log("Waiting for events...");

    changeStream.on("change", async (change) => {

      console.log("---------------------------------");
      console.log("Event received:", change.operationType);

      if (change.operationType === "insert") {

        const order = change.fullDocument;

        await processOrder(order);
      }
    });

  } catch (err) {

    console.error("Error:", err);
  }
}

run();