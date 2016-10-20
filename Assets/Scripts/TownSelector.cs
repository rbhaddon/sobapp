using UnityEngine;
using System.Collections;
using UnityEngine.UI;

public class TownSelector : MonoBehaviour {

	public int townIndex;
	public GameObject townPanel;

	private Renderer rend;

	void Start() {
		//Debug.LogWarning ("TownSelector Start");
		rend = GetComponent<Renderer>();
	}
	void OnMouseEnter() {
		rend.material.color = Color.magenta;
		//Debug.Log ("MouseEnter");
	}
	void OnMouseOver() {
		//rend.material.color -= new Color(0.1F, 0, 0) * Time.deltaTime;
	}
	void OnMouseExit() {
		rend.material.color = Color.white;
		//Debug.Log ("MouseExit");
	}

	void OnMouseDown() {
		GameControl.currentTown = GameControl.gameData.towns [townIndex];
		townPanel.SetActive (true);

//		Text[] townPanelTexts = townPanel.GetComponentsInChildren<Text>();
//
//		foreach (Text text in townPanelTexts) {
//			if (text.name == "TownNameText") {
//				text.text = town.name;
//				break;
//			}
//		}

	}
}