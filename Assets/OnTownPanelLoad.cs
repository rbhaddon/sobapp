using UnityEngine;
using System.Collections;
using System;
using UnityEngine.UI;
using HexCrawlConstants;

public class OnTownPanelLoad : MonoBehaviour {

	public Town town;

	// Use this for initialization
	void Start ()
	{
		Debug.Log ("OnTownPanelLoad.Start()");
	}

	void OnEnable () {
		Debug.Log ("OnTownPanelLoad.OnEnable()");
		town = GameControl.currentTown;

		Text[] townPanelTexts = GetComponentsInChildren<Text>();

		foreach (Text text in townPanelTexts) {
			if (text.name == "TownNameText") {
				text.text = town.name;
				break;
			}
		}
	}
	
	// Update is called once per frame
	void Update () {
	
	}
}
