using UnityEngine;
using System.Collections;
using UnityEngine.EventSystems;

public class SelectTownOnClick : MonoBehaviour {

	public GameObject townPanel;

	public void LoadTownByName(string townName) {
		townPanel.GetComponent<GUIText> ().text = townName;
		townPanel.SetActive (true);
	}
}