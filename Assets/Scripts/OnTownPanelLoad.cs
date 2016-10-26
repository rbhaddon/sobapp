using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System;
using UnityEngine.UI;
using HexCrawlConstants;

public class OnTownPanelLoad : MonoBehaviour {

	public Text[] townPanelTexts;
	public GameObject locationPanel;
	public GameObject locationText;
	List<GameObject> locTexts = new List<GameObject> ();

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
		foreach (GameObject gObject in locTexts) {
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
	
		locTexts.Clear ();

		if (GameControl.currentTown.status == TownData.Status.Okay) {

			for (int i = 0; i < GameControl.currentTown.locations.Count; i++) {
				//foreach (TownData.LocationType location in GameControl.currentTown.locations) {
				locTexts.Add (Instantiate (locationText));
				locTexts [i].transform.SetParent (locationPanel.transform);
				Text text = locTexts [i].GetComponent<Text> ();
				text.text = TownData.Locations[GameControl.currentTown.locations [i]];
				//GameObject locText = Instantiate (locationText);
				//locText.transform.SetParent (locationPanel.transform);
			}
			GameControl.prevTownKey = GameControl.currentTownKey;
		}
	}
}
