import assert from "node:assert/strict";
import { describe, it } from "node:test";
import { convertOvenToAirfryer } from "./airfryer-omregning.ts";
import { resolveEquipment } from "./recipe-equipment.ts";

describe("convertOvenToAirfryer", () => {
  it("varmluft: 200 °C / 40 min → 180 °C / 32 min", () => {
    const result = convertOvenToAirfryer(200, 40, "varmluft");
    assert.equal(result.temp, 180);
    assert.equal(result.checkAt, 32);
    assert.equal(result.timeFactor, 0.8);
  });

  it("over/undervarme: 200 °C / 40 min → 190 °C / 30 min", () => {
    const result = convertOvenToAirfryer(200, 40, "over-undervarme");
    assert.equal(result.temp, 190);
    assert.equal(result.checkAt, 30);
    assert.equal(result.timeFactor, 0.75);
  });
});

describe("resolveEquipment", () => {
  it("uses category default when equipment is missing", () => {
    assert.deepEqual(resolveEquipment({ category: "grill" }), [
      { id: "grill", label: "Grill" },
    ]);
  });

  it("prefers explicit equipment overrides", () => {
    assert.deepEqual(
      resolveEquipment({
        category: "airfryer",
        equipment: [
          { id: "airfryer", label: "8L Airfryer" },
          { id: "meater", label: "MEATER-probe" },
        ],
      }),
      [
        { id: "airfryer", label: "8L Airfryer" },
        { id: "meater", label: "MEATER-probe" },
      ],
    );
  });
});
