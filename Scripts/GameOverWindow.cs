using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class GameOverWindow : MonoBehaviour
{
    public Text winnerName;
    public Button restartButton;
    
    void Awake()
    {
        restartButton.onClick.AddListener(OnClick);
    }
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void SetName(string s)
    {
        winnerName.text = s;
    }
    public void OnClick()
    {
        SceneManager.LoadScene("SampleScene");
    }
}
