using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class CalendarButtonOnClick : MonoBehaviour {

	public Text buttonText;

	// Use this for initialization
//	void Start () {
//		buttonText = gameObject.GetComponent<Text> ();
//	}
	
	void FixedUpdate () {
		if (buttonText) {
			buttonText.text = "Day: " + GameControl.gameData.day.ToString ();
		}
	}

	public void NextDay()
	{
		GameControl.gameData.NextDay ();
	}
}
