import assert from "node:assert/strict";
import { describe, it } from "node:test";
import { INGREDIENT_NAV } from "./ingredient-nav.ts";
import {
  lineMatchesAlias,
  normalizeIngredientLine,
  recipeMatchesIngredient,
} from "./ingredient-match.ts";

describe("normalizeIngredientLine", () => {
  it("fjerner mængde foran kartoffel-linje", () => {
    assert.equal(
      normalizeIngredientLine("8 mellemstore kartofler, ens størrelse"),
      "mellemstore kartofler, ens størrelse"
    );
  });

  it("fjerner gram-mængde og parenteser", () => {
    assert.equal(
      normalizeIngredientLine("500 g hakket kalv og svin (eller blandet hakket)"),
      "hakket kalv og svin"
    );
  });

  it("bevarer link-tekst fra markdown", () => {
    assert.match(
      normalizeIngredientLine(
        "[Bøgerøget flagesalt](/opskrifter/roeg/roget-salt) eller ramsløgssalt"
      ),
      /bøgerøget flagesalt/
    );
  });

  it("håndterer brøk-mængder", () => {
    assert.equal(normalizeIngredientLine("½ tsk muskatnød"), "muskatnød");
  });
});

describe("lineMatchesAlias", () => {
  it("matcher kartofler → kartoffel", () => {
    assert.equal(
      lineMatchesAlias("8 mellemstore kartofler, ens størrelse", "kartofler"),
      true
    );
  });

  it("matcher løg i «1 lille løg, finthakket»", () => {
    assert.equal(lineMatchesAlias("1 lille løg, finthakket", "løg"), true);
  });

  it("matcher ikke laks i lakrids", () => {
    assert.equal(lineMatchesAlias("1 tsk lakrids pulver", "laks"), false);
  });

  it("matcher ikke and inde i blandet", () => {
    assert.equal(lineMatchesAlias("500 g blandet hakket", "and"), false);
  });

  it("matcher hel and", () => {
    assert.equal(lineMatchesAlias("1 hel and (ca. 2 kg)", "and"), true);
  });

  it("matcher ikke oliven på en smør-linje", () => {
    assert.equal(lineMatchesAlias("2 spsk smør", "oliven"), false);
  });
});

describe("recipeMatchesIngredient", () => {
  const kartoffel = INGREDIENT_NAV.find((i) => i.slug === "kartoffel")!;
  const loeg = INGREDIENT_NAV.find((i) => i.slug === "loeg")!;
  const laks = INGREDIENT_NAV.find((i) => i.slug === "laks")!;

  it("finder kartoffel-opskrift", () => {
    assert.equal(
      recipeMatchesIngredient(
        { ingredients: ["8 mellemstore kartofler", "75 g smør"] },
        kartoffel
      ),
      true
    );
  });

  it("finder løg i frikadelle-farce", () => {
    assert.equal(
      recipeMatchesIngredient(
        {
          ingredients: [
            "500 g hakket kalv og svin (eller blandet hakket)",
            "1 lille løg, finthakket",
            "1 æg",
          ],
        },
        loeg
      ),
      true
    );
  });

  it("matcher ikke laks på opskrift uden laks", () => {
    assert.equal(
      recipeMatchesIngredient(
        { ingredients: ["1 tsk lakrids", "200 g sukker"] },
        laks
      ),
      false
    );
  });
});
