using UnityEngine;
using System.Collections;
using UnityEngine.UI;
using System;

public class RollAilmentChart : MonoBehaviour {

	public InputField rollInputField;
	public Text ailmentTitleText;
	public Text ailmentNameText;
	public Text ailmentRollText;
	public Text ailmentFlavorText;
	public Text ailmentEffectText;

	int ReRoll() {
		int roll = Roll.D36 ();
		rollInputField.text = roll.ToString ();

		return roll;
	}

	public void OnClick () {
		int roll = 0;

		if (Int32.TryParse (rollInputField.text, out roll)) {
			if (roll < 11 || roll > 66) {
				roll = ReRoll ();
			}
		} else {
			roll = ReRoll ();
		}

		Ailment ailment;
		switch (ailmentTitleText.text)
		{
		case "Injury":
			ailment = GameControl.gameData.injury [roll];
			break;
		case "Madness":
			ailment = GameControl.gameData.madness [roll];
			break;
		case "Mutation":
			ailment = GameControl.gameData.mutation [roll];
			break;
		default:
			Debug.Log ("No ailment chart found!");
			ailment = new Ailment ();
			ailment.name = "Not Found";
			ailment.flavor = "";
			ailment.effect = "";
			break;
		}

		ailmentNameText.text = ailment.name;
		ailmentRollText.text = roll.ToString ();
		ailmentFlavorText.text = ailment.flavor;
		ailmentEffectText.text = ailment.effect;

		rollInputField.text = "";
	}
}