using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System;
using UnityEngine.UI;
using HexCrawlConstants;

public class OnTownPanelLoad : MonoBehaviour {

	public Text[] townPanelTexts;
	public GameObject locationPanel;
	public GameObject locationButton;
	List<GameObject> locationButtons = new List<GameObject> ();

	Town currentTown;

	// Use this for initialization
	void Start ()
	{
		Debug.Log ("OnTownPanelLoad.Start()");
		townPanelTexts = GetComponentsInChildren<Text>();
	}

	void Update () {
		if (GameControl.TownChanged ()) {
			DisplayTownData ();
		}
	}

	void DisplayTownData()
	{
		// Clear any previous town's location buttons
		foreach (GameObject gObject in locationButtons) {
			Destroy (gObject);
		}
			
		//Debug.Log ("OnTownPanelLoad.OnEnable()");
		//town = GameControl.currentTown;
		//if (GameControl.TownChanged ()) {
		if (townPanelTexts != null) {
			foreach (Text text in townPanelTexts) {
				switch (text.name) {
				case "TownNameText":
					text.text = GameControl.currentTown.name;
					break;
				case "TownSizeText":
					text.text = "Size: " + GameControl.currentTown.size.ToString ();
					break;
				case "TownTypeText":
					text.text = "Type: " + GameControl.currentTown.type;
					break;
				case "TownTraitName":
					text.text = "Trait: " + GameControl.currentTown.trait.name;
					break;
				default:
					break;
				}
			}
		}
	
		locationButtons.Clear ();

		if (GameControl.currentTown.status == TownData.Status.Okay) {

			for (int i = 0; i < GameControl.currentTown.locations.Count; i++) {
				locationButtons.Add (Instantiate (locationButton));
				locationButtons [i].transform.SetParent (locationPanel.transform);
				Text text = locationButtons [i].GetComponentInChildren<Text> ();
				text.text = TownData.Locations[GameControl.currentTown.locations [i]];
			}
			GameControl.prevTownKey = GameControl.currentTownKey;
		}
	}
}
