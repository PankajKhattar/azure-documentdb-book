const { MongoClient } = require("mongodb");

async function run() {

  const client = new MongoClient(
    "mongodb://localhost:27017"
  );

  try {

    await client.connect();

    const db = client.db("shop");

    const collection = db.collection("orders");

    const result = await collection.updateOne(
      {
        _id: "order_101"
      },
      {
        $setOnInsert: {
          customerId: "C123",
          amount: 1500,
          status: "created"
        }
      },
      {
        upsert: true
      }
    );

    console.log("Idempotent operation completed");

    console.log(result);

  } catch (err) {

    console.error(err);

  } finally {

    await client.close();
  }
}

run();